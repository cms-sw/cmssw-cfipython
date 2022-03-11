import FWCore.ParameterSet.Config as cms

alCaRecoTriggerBitsRcdRead = cms.EDAnalyzer('AlCaRecoTriggerBitsRcdRead',
  rawFileName = cms.untracked.string(''),
  outputType = cms.untracked.string('twiki'),
  mightGet = cms.optional.untracked.vstring
)
