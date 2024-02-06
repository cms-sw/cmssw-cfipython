import FWCore.ParameterSet.Config as cms

ecalRawToDigiPortable = cms.EDProducer('EcalRawToDigiPortable@alpaka',
  InputLabel = cms.InputTag('rawDataCollector'),
  FEDs = cms.vint32(
    601,
    602,
    603,
    604,
    605,
    606,
    607,
    608,
    609,
    610,
    611,
    612,
    613,
    614,
    615,
    616,
    617,
    618,
    619,
    620,
    621,
    622,
    623,
    624,
    625,
    626,
    627,
    628,
    629,
    630,
    631,
    632,
    633,
    634,
    635,
    636,
    637,
    638,
    639,
    640,
    641,
    642,
    643,
    644,
    645,
    646,
    647,
    648,
    649,
    650,
    651,
    652,
    653,
    654
  ),
  maxChannelsEB = cms.uint32(61200),
  maxChannelsEE = cms.uint32(14648),
  digisLabelEB = cms.string('ebDigis'),
  digisLabelEE = cms.string('eeDigis'),
  mightGet = cms.optional.untracked.vstring,
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
