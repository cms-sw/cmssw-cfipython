import FWCore.ParameterSet.Config as cms

def L1TSC82ProngJetProducer(*args, **kwargs):
  mod = cms.EDProducer('L1TSC82ProngJetProducer',
    jets = cms.InputTag('l1tSC8PFL1PuppiEmulator'),
    l1tSC82ProngJetModelPath = cms.string('L1TSC82ProngJetModel_v0'),
    minPt = cms.double(0),
    maxEta = cms.double(5),
    maxJets = cms.int32(16),
    nParticles = cms.int32(8),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
