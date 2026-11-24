import FWCore.ParameterSet.Config as cms

def alpaka_rocm_async_onnxtest_DataSource(*args, **kwargs):
  mod = cms.EDProducer('alpaka_rocm_async::onnxtest::DataSource',
    sizes = cms.vuint32(35),
    mightGet = cms.optional.untracked.vstring,
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string(''),
      synchronize = cms.optional.untracked.bool
    )
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
