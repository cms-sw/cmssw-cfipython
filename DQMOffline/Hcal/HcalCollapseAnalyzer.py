import FWCore.ParameterSet.Config as cms

def HcalCollapseAnalyzer(*args, **kwargs):
  mod = cms.EDProducer('HcalCollapseAnalyzer',
    topFolderName = cms.string('HcalCollapse'),
    verbosity = cms.untracked.int32(0),
    recHitHBHE = cms.untracked.InputTag('hbhereco'),
    preRecHitHBHE = cms.untracked.InputTag('hbheprereco'),
    doHE = cms.untracked.bool(True),
    doHB = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
