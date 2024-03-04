import FWCore.ParameterSet.Config as cms

def CosmicRateAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('CosmicRateAnalyzer',
    tracksInputTag = cms.InputTag('ALCARECOTkAlCosmicsCTF0T'),
    muonsInputTag = cms.InputTag('muons1Leg'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
