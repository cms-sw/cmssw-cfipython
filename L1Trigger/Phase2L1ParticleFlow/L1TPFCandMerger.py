import FWCore.ParameterSet.Config as cms

def L1TPFCandMerger(**kwargs):
  mod = cms.EDProducer('L1TPFCandMerger',
    src = cms.VInputTag(
      'collection1',
      'collection2'
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
