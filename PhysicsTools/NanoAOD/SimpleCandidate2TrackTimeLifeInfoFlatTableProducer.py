import FWCore.ParameterSet.Config as cms

def SimpleCandidate2TrackTimeLifeInfoFlatTableProducer(**kwargs):
  mod = cms.EDProducer('SimpleCandidate2TrackTimeLifeInfoFlatTableProducer',
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
    singleton = cms.bool(False),
    cut = cms.string(''),
    maxLen = cms.optional.uint32,
    externalVariables = cms.PSet(),
    externalTypedVariables = cms.PSet(),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod