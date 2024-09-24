import FWCore.ParameterSet.Config as cms

def GlobalVariablesTableProducer(*args, **kwargs):
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
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
