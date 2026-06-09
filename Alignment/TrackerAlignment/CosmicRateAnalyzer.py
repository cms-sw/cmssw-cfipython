import FWCore.ParameterSet.Config as cms

def CosmicRateAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('CosmicRateAnalyzer',
    tracksInputTag = cms.InputTag('ALCARECOTkAlCosmicsCTF0T'),
    muonsInputTag = cms.InputTag('muons1Leg'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
