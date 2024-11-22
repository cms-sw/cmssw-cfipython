import FWCore.ParameterSet.Config as cms

def LHEGenericMassFilter(*args, **kwargs):
  mod = cms.EDFilter('LHEGenericMassFilter',
    src = cms.InputTag('externalLHEProducer'),
    NumRequired = cms.int32(1),
    ParticleID = cms.vint32(1),
    MinMass = cms.double(0),
    MaxMass = cms.double(1),
    RequiredOutgoingStatus = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
