import FWCore.ParameterSet.Config as cms

def L1SeedConePFJetProducer(*args, **kwargs):
  mod = cms.EDProducer('L1SeedConePFJetProducer',
    L1PFObjects = cms.InputTag('l1tLayer1', 'Puppi'),
    nJets = cms.uint32(16),
    coneSize = cms.double(0.4),
    HW = cms.bool(False),
    debug = cms.bool(False),
    doCorrections = cms.bool(False),
    correctorFile = cms.string(''),
    correctorDir = cms.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
