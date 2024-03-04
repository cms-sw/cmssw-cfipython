import FWCore.ParameterSet.Config as cms

def HcalCollapseAnalyzer(**kwargs):
  mod = cms.EDProducer('HcalCollapseAnalyzer',
    topFolderName = cms.string('HcalCollapse'),
    verbosity = cms.untracked.int32(0),
    recHitHBHE = cms.untracked.InputTag('hbhereco'),
    preRecHitHBHE = cms.untracked.InputTag('hbheprereco'),
    doHE = cms.untracked.bool(True),
    doHB = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
