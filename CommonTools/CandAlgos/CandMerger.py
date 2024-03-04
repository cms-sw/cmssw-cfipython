import FWCore.ParameterSet.Config as cms

def CandMerger(**kwargs):
  mod = cms.EDProducer('CandMerger',
    src = cms.VInputTag(
      'collection1',
      'collection2'
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
