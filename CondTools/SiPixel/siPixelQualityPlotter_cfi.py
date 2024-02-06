import FWCore.ParameterSet.Config as cms

siPixelQualityPlotter = cms.EDAnalyzer('SiPixelQualityPlotter',
  useLogScale = cms.bool(False),
  addLumiInfo = cms.bool(True),
  analyzedTag = cms.string(''),
  maxRun = cms.untracked.uint32(999999),
  lumiInputTag = cms.untracked.InputTag(''),
  mightGet = cms.optional.untracked.vstring
)
