import FWCore.ParameterSet.Config as cms

def HLTEgammaDoubleEtPhiFilter(*args, **kwargs):
  mod = cms.EDFilter('HLTEgammaDoubleEtPhiFilter',
    saveTags = cms.bool(True),
    candTag = cms.InputTag('hltDoubleL1MatchFilter'),
    etcut1 = cms.double(6),
    etcut2 = cms.double(6),
    MinAcop = cms.double(-0.1),
    MaxAcop = cms.double(0.6),
    MinEtBalance = cms.double(-1),
    MaxEtBalance = cms.double(10),
    npaircut = cms.int32(1),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
