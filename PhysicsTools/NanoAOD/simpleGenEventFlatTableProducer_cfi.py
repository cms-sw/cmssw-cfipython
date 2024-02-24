import FWCore.ParameterSet.Config as cms

simpleGenEventFlatTableProducer = cms.EDProducer('SimpleGenEventFlatTableProducer',
  name = cms.required.string,
  doc = cms.string(''),
  extension = cms.bool(False),
  skipNonExistingSrc = cms.bool(False),
  src = cms.required.InputTag,
  variables = cms.PSet(
    allowAnyLabel_ = cms.required.PSetTemplate(
      expr = cms.required.string,
      doc = cms.required.string,
      type = cms.string('int')
    )
  ),
  mightGet = cms.optional.untracked.vstring
)
