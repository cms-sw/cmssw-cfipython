import FWCore.ParameterSet.Config as cms

def SiStripLorentzAnglePCLHarvester(**kwargs):
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
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
