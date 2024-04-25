import FWCore.ParameterSet.Config as cms

simplePATMuon2TrackTimeLifeInfoFlatTableProducer = cms.EDProducer('SimplePATMuon2TrackTimeLifeInfoFlatTableProducer',
  name = cms.required.string,
  doc = cms.string(''),
  extension = cms.bool(False),
  skipNonExistingSrc = cms.bool(False),
  src = cms.required.InputTag,
  variables = cms.PSet(),
  singleton = cms.bool(False),
  cut = cms.string(''),
  lazyEval = cms.untracked.bool(False),
  maxLen = cms.optional.uint32,
  externalVariables = cms.PSet(),
  externalTypedVariables = cms.PSet(),
  mightGet = cms.optional.untracked.vstring
)
