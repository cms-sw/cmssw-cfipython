import FWCore.ParameterSet.Config as cms

def L1TZDCAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('L1TZDCAnalyzer',
    etSumTag = cms.InputTag('etSumZdcProducer'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
