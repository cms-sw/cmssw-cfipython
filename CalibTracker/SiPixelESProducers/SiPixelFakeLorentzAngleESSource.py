import FWCore.ParameterSet.Config as cms

def SiPixelFakeLorentzAngleESSource(*args, **kwargs):
  mod = cms.ESSource('SiPixelFakeLorentzAngleESSource',
    file = cms.FileInPath('SLHCUpgradeSimulations/Geometry/data/PhaseI/PixelSkimmedGeometry_phase1.txt'),
    topologyInput = cms.FileInPath('Geometry/TrackerCommonData/data/PhaseI/trackerParameters.xml'),
    appendToDataLabel = cms.string(''),
    bPixLorentzAnglePerTesla = cms.untracked.double(-9999),
    fPixLorentzAnglePerTesla = cms.untracked.double(-9999),
    BPixParameters = cms.VPSet(
      template = cms.PSetTemplate(
        layer = cms.optional.int32,
        ladder = cms.optional.int32,
        module = cms.optional.int32,
        side = cms.optional.int32,
        angle = cms.required.double
      )
    ),
    FPixParameters = cms.VPSet(
      template = cms.PSetTemplate(
        side = cms.optional.int32,
        disk = cms.optional.int32,
        ring = cms.optional.int32,
        blade = cms.optional.int32,
        panel = cms.optional.int32,
        HVgroup = cms.optional.int32,
        angle = cms.required.double
      )
    ),
    ModuleParameters = cms.VPSet(
      template = cms.PSetTemplate(
        rawid = cms.required.uint32,
        angle = cms.required.double
      )
    )
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
