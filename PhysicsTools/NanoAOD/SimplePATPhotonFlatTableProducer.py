import FWCore.ParameterSet.Config as cms

def SimplePATPhotonFlatTableProducer(*args, **kwargs):
  mod = cms.EDProducer('SimplePATPhotonFlatTableProducer',
    name = cms.required.string,
    doc = cms.string(''),
    extension = cms.bool(False),
    skipNonExistingSrc = cms.bool(False),
    src = cms.required.InputTag,
    variables = cms.PSet(
      allowAnyLabel_ = cms.required.PSetTemplate(
        expr = cms.required.string,
        doc = cms.required.string,
        lazyEval = cms.untracked.bool(False),
        type = cms.string('int')
      )
    ),
    singleton = cms.bool(False),
    cut = cms.string(''),
    lazyEval = cms.untracked.bool(False),
    maxLen = cms.optional.uint32,
    externalVariables = cms.PSet(),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
