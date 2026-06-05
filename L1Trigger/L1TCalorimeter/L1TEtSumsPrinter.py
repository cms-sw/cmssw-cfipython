import FWCore.ParameterSet.Config as cms

def L1TEtSumsPrinter(*args, **kwargs):
  mod = cms.EDAnalyzer('L1TEtSumsPrinter',
    src = cms.InputTag('gtStage2Digis', 'EtSum'),
    etSumTypes = cms.vint32(),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
