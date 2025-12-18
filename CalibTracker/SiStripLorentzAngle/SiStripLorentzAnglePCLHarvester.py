import FWCore.ParameterSet.Config as cms

def SiStripLorentzAnglePCLHarvester(*args, **kwargs):
  mod = cms.EDProducer('SiStripLorentzAnglePCLHarvester',
    debugMode = cms.bool(False),
    dqmDir = cms.string('AlCaReco/SiStripLorentzAngle'),
    fitRange = cms.vdouble(
      0,
      0
    ),
    record = cms.string('SiStripLorentzAngleRcd'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
