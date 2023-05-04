import FWCore.ParameterSet.Config as cms

siPixelLorentzAngleReader = cms.EDAnalyzer('SiPixelLorentzAngleReader',
  recoLabel = cms.string(''),
  simLabel = cms.string(''),
  printDebug = cms.untracked.uint32(10),
  useSimRcd = cms.bool(False),
  mightGet = cms.optional.untracked.vstring
)
