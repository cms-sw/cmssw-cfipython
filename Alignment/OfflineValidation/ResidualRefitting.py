import FWCore.ParameterSet.Config as cms

def ResidualRefitting(*args, **kwargs):
  mod = cms.EDAnalyzer('ResidualRefitting',
    muons = cms.InputTag('muons'),
    muonsRemake = cms.InputTag('globalMuons'),
    muonsNoStation1 = cms.InputTag('muonsNoSt1'),
    muonsNoStation2 = cms.InputTag('muonsNoSt2'),
    muonsNoStation3 = cms.InputTag('muonsNoSt3'),
    muonsNoStation4 = cms.InputTag('muonsNoSt4'),
    histoutputFile = cms.untracked.string('histFile.root'),
    doDebug = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
