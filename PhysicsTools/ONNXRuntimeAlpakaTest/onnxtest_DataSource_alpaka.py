import FWCore.ParameterSet.Config as cms

def onnxtest_DataSource_alpaka(*args, **kwargs):
  mod = cms.EDProducer('onnxtest::DataSource@alpaka',
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
