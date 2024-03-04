import FWCore.ParameterSet.Config as cms

def test_PedestalsBuilder(**kwargs):
  mod = cms.EDAnalyzer('test_PedestalsBuilder',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
