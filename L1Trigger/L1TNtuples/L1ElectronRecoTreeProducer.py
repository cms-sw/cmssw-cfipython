import FWCore.ParameterSet.Config as cms

def L1ElectronRecoTreeProducer(**kwargs):
  mod = cms.EDAnalyzer('L1ElectronRecoTreeProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
