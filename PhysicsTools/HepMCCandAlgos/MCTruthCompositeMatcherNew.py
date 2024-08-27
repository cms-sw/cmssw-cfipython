import FWCore.ParameterSet.Config as cms

def MCTruthCompositeMatcherNew(**kwargs):
  mod = cms.EDProducer('MCTruthCompositeMatcherNew',
    src = cms.required.InputTag,
    matchMaps = cms.required.VInputTag,
    matchPDGId = cms.required.vint32,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
