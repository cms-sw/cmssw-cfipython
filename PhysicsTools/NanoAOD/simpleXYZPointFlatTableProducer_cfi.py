import FWCore.ParameterSet.Config as cms

simpleXYZPointFlatTableProducer = cms.EDProducer('SimpleXYZPointFlatTableProducer',
  name = cms.required.string,
  doc = cms.string(''),
  extension = cms.bool(False),
  skipNonExistingSrc = cms.bool(False),
  src = cms.required.InputTag,
  variables = cms.PSet(),
  mightGet = cms.optional.untracked.vstring
)
