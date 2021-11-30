import FWCore.ParameterSet.Config as cms

siPixelFakeLorentzAngleESSource = cms.ESSource('SiPixelFakeLorentzAngleESSource',
  file = cms.FileInPath('SLHCUpgradeSimulations/Geometry/data/PhaseI/PixelSkimmedGeometry_phase1.txt'),
  topologyInput = cms.FileInPath('Geometry/TrackerCommonData/data/PhaseI/trackerParameters.xml'),
  label = cms.string(''),
  bPixLorentzAnglePerTesla = cms.untracked.double(-9999),
  fPixLorentzAnglePerTesla = cms.untracked.double(-9999),
  BPixParameters = cms.VPSet(
  ),
  FPixParameters = cms.VPSet(
  ),
  ModuleParameters = cms.VPSet(
  ),
  appendToDataLabel = cms.string('')
)
