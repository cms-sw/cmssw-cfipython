import FWCore.ParameterSet.Config as cms

def HLTHPDFilter(**kwargs):
  mod = cms.EDFilter('HLTHPDFilter',
    inputTag = cms.InputTag('hltHbhereco'),
    energy = cms.double(-99),
    hpdSpikeEnergy = cms.double(10),
    hpdSpikeIsolationEnergy = cms.double(1),
    rbxSpikeEnergy = cms.double(50),
    rbxSpikeUnbalance = cms.double(0.2),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
