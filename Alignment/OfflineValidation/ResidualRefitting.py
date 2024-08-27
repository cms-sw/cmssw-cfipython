import FWCore.ParameterSet.Config as cms

def ResidualRefitting(**kwargs):
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
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
