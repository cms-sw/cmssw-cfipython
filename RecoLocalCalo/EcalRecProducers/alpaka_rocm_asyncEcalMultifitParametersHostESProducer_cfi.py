import FWCore.ParameterSet.Config as cms

alpaka_rocm_asyncEcalMultifitParametersHostESProducer = cms.ESProducer('alpaka_rocm_async::EcalMultifitParametersHostESProducer',
  EBtimeFitParameters = cms.vdouble(
    -2.015452,
    3.130702,
    -12.3473,
    41.88921,
    -82.83944,
    91.01147,
    -50.35761,
    11.05621
  ),
  EEtimeFitParameters = cms.vdouble(
    -2.390548,
    3.553628,
    -17.62341,
    67.67538,
    -133.213,
    140.7432,
    -75.41106,
    16.20277
  ),
  EBamplitudeFitParameters = cms.vdouble(
    1.138,
    1.652
  ),
  EEamplitudeFitParameters = cms.vdouble(
    1.89,
    1.4
  ),
  appendToDataLabel = cms.string(''),
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
