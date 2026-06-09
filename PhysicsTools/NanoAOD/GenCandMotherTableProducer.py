import FWCore.ParameterSet.Config as cms

def GenCandMotherTableProducer(*args, **kwargs):
  mod = cms.EDProducer('GenCandMotherTableProducer',
    objName = cms.string('GenCands'),
    branchName = cms.string('GenPart'),
    src = cms.InputTag('packedGenParticles'),
    mcMap = cms.InputTag('finalGenParticles'),
    genparticles = cms.InputTag('finalGenparticles'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
