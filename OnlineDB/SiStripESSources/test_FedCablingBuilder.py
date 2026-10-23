import FWCore.ParameterSet.Config as cms

def test_FedCablingBuilder(*args, **kwargs):
  mod = cms.EDAnalyzer('test_FedCablingBuilder',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
