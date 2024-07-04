import FWCore.ParameterSet.Config as cms

alpaka_cuda_asyncHcalMahiPulseOffsetsESProducer = cms.ESProducer('alpaka_cuda_async::HcalMahiPulseOffsetsESProducer',
  pulseOffsets = cms.vint32(
    -3,
    -2,
    -1,
    0,
    1,
    2,
    3,
    4
  ),
  appendToDataLabel = cms.string(''),
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
