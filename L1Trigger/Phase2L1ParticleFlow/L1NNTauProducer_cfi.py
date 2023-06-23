import FWCore.ParameterSet.Config as cms

L1NNTauProducer = cms.EDProducer('L1NNTauProducer',
  NNFileName = cms.string('L1Trigger/Phase2L1ParticleFlow/data/tau_3layer.pb'),
  tausize = cms.double(0.1),
  maxtaus = cms.int32(5),
  nparticles = cms.int32(10),
  conesize = cms.double(0.4),
  seedpt = cms.double(20),
  HW = cms.bool(True),
  emseed = cms.bool(True),
  debug = cms.bool(False),
  L1PFObjects = cms.InputTag('L1PFProducer', 'l1pfCandidates'),
  mightGet = cms.optional.untracked.vstring
)
