import FWCore.ParameterSet.Config as cms

def P2GTCandidateAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('P2GTCandidateAnalyzer',
    l1GTAlgoBlockTag = cms.InputTag('l1tGTProducer', 'AlgoBlocks'),
    l1GTAlgoNames = cms.vstring(),
    objectType = cms.string('GMTTkMuons'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
