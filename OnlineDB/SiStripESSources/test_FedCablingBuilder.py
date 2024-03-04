import FWCore.ParameterSet.Config as cms

def test_FedCablingBuilder(**kwargs):
  mod = cms.EDAnalyzer('test_FedCablingBuilder',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
