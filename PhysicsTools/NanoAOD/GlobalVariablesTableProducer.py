import FWCore.ParameterSet.Config as cms

def GlobalVariablesTableProducer(**kwargs):
  mod = cms.EDProducer('GlobalVariablesTableProducer',
    name = cms.string(''),
    extension = cms.bool(False),
    variables = cms.PSet(
      allowAnyLabel_ = cms.required.PSetTemplate(
        type = cms.string('int'),
        src = cms.required.InputTag,
        doc = cms.required.string,
        precision = cms.int32(-1)
      )
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
