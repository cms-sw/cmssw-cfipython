import FWCore.ParameterSet.Config as cms

def L1MetFilterRecoTreeProducer(**kwargs):
  mod = cms.EDAnalyzer('L1MetFilterRecoTreeProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
