import FWCore.ParameterSet.Config as cms

def alpaka_cuda_async_EcalRecHitParametersESProducer(*args, **kwargs):
  mod = cms.ESProducer('alpaka_cuda_async::EcalRecHitParametersESProducer',
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
      kNeighboursRecovered = cms.vstring(
        'kFixedG0',
        'kNonRespondingIsolated',
        'kDeadVFE'
      ),
      kDead = cms.vstring('kNoDataNoTP'),
      kNoisy = cms.vstring(
        'kNNoisy',
        'kFixedG6',
        'kFixedG1'
      ),
      kTowerRecovered = cms.vstring('kDeadFE')
    ),
    appendToDataLabel = cms.string(''),
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string(''),
      synchronize = cms.optional.untracked.bool
    )
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
