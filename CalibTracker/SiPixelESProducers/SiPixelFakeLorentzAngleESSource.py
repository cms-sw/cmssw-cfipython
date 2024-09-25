import FWCore.ParameterSet.Config as cms

def SiPixelFakeLorentzAngleESSource(*args, **kwargs):
  mod = cms.ESSource('SiPixelFakeLorentzAngleESSource',
    file = cms.FileInPath('SLHCUpgradeSimulations/Geometry/data/PhaseI/PixelSkimmedGeometry_phase1.txt'),
    topologyInput = cms.FileInPath('Geometry/TrackerCommonData/data/PhaseI/trackerParameters.xml'),
    appendToDataLabel = cms.string(''),
    bPixLorentzAnglePerTesla = cms.untracked.double(-9999),
    fPixLorentzAnglePerTesla = cms.untracked.double(-9999),
    BPixParameters = cms.VPSet(
    ),
    FPixParameters = cms.VPSet(
    ),
    ModuleParameters = cms.VPSet(
    )
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
