import FWCore.ParameterSet.Config as cms

def EcalEBTrigPrimPhase2SpikeTaggerESProducer(*args, **kwargs):
  mod = cms.ESProducer('EcalEBTrigPrimPhase2SpikeTaggerESProducer',
    fwVersion = cms.uint32(1),
    algoConfigs = cms.VPSet(
      cms.PSet(),
      template = cms.PSetTemplate(
        algo = cms.string('ld'),
        perCrystalParams = cms.VPSet(
          cms.PSet(),
          template = cms.PSetTemplate(
            ietaRange = cms.string(':'),
            iphiRange = cms.string(':'),
            peakSampleIndex = cms.uint32(5),
            spikeThreshold = cms.double(-0.1),
            weights = cms.vdouble(
              1.5173,
              -2.1034,
              1.8117,
              -0.6451
            )
          )
        )
      )
    ),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
