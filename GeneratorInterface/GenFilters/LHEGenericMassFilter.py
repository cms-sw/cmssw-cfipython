import FWCore.ParameterSet.Config as cms

def LHEGenericMassFilter(**kwargs):
  mod = cms.EDFilter('LHEGenericMassFilter',
    src = cms.InputTag('externalLHEProducer'),
    NumRequired = cms.int32(1),
    ParticleID = cms.vint32(1),
    MinMass = cms.double(0),
    MaxMass = cms.double(1),
    RequiredOutgoingStatus = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
