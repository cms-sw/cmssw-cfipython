import FWCore.ParameterSet.Config as cms

def L1TEtSumsPrinter(**kwargs):
  mod = cms.EDAnalyzer('L1TEtSumsPrinter',
    src = cms.InputTag('gtStage2Digis', 'EtSum'),
    etSumTypes = cms.vint32(),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
