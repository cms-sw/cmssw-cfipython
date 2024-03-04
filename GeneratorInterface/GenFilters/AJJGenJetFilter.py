import FWCore.ParameterSet.Config as cms

def AJJGenJetFilter(**kwargs):
  mod = cms.EDFilter('AJJGenJetFilter',
    GenJetCollection = cms.InputTag('ak4GenJetsNoNu'),
    genParticles = cms.InputTag('genParticles'),
    minPt = cms.double(-1),
    minEta = cms.double(-5),
    maxEta = cms.double(5),
    deltaRJetLep = cms.double(0),
    minDeltaEta = cms.double(0),
    maxDeltaEta = cms.double(9999),
    MinInvMass = cms.double(0),
    maxPhotonEta = cms.double(5),
    minPhotonPt = cms.double(50),
    maxPhotonPt = cms.double(10000),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
