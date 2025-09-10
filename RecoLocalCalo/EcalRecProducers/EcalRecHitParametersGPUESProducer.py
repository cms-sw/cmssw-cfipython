import FWCore.ParameterSet.Config as cms

def EcalRecHitParametersGPUESProducer(*args, **kwargs):
  mod = cms.ESSource('EcalRecHitParametersGPUESProducer',
    ChannelStatusToBeExcluded = cms.vstring(
      'kDAC',
      'kNoisy',
      'kNNoisy',
      'kFixedG6',
      'kFixedG1',
      'kFixedG0',
      'kNonRespondingIsolated',
      'kDeadVFE',
      'kDeadFE',
      'kNoDataNoTP'
    ),
    flagsMapDBReco = cms.PSet(
      kGood = cms.vstring(
        'kOk',
        'kDAC',
        'kNoLaser',
        'kNoisy'
      ),
      kNoisy = cms.vstring(
        'kNNoisy',
        'kFixedG6',
        'kFixedG1'
      ),
      kNeighboursRecovered = cms.vstring(
        'kFixedG0',
        'kNonRespondingIsolated',
        'kDeadVFE'
      ),
      kTowerRecovered = cms.vstring('kDeadFE'),
      kDead = cms.vstring('kNoDataNoTP')
    ),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
