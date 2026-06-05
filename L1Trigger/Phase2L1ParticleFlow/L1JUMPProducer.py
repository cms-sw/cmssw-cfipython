import FWCore.ParameterSet.Config as cms

def L1JUMPProducer(*args, **kwargs):
  mod = cms.EDProducer('L1JUMPProducer',
    RawMET = cms.InputTag('l1tMETPFProducer'),
    L1PFJets = cms.InputTag('l1tSC4PFL1PuppiCorrectedEmulator'),
    MinJetpT = cms.double(30),
    MaxJetEta = cms.double(3),
    JERFile = cms.string('L1Trigger/Phase2L1ParticleFlow/data/met/l1jump_jer_v1.json'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
