import FWCore.ParameterSet.Config as cms

simpleHTXSFlatTableProducer = cms.EDProducer('SimpleHTXSFlatTableProducer',
  name = cms.required.string,
  doc = cms.string(''),
  extension = cms.bool(False),
  skipNonExistingSrc = cms.bool(False),
  src = cms.required.InputTag,
  variables = cms.PSet(),
  mightGet = cms.optional.untracked.vstring
)
