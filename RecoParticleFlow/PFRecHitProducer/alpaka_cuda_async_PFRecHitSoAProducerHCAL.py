import FWCore.ParameterSet.Config as cms

def alpaka_cuda_async_PFRecHitSoAProducerHCAL(*args, **kwargs):
  mod = cms.EDProducer('alpaka_cuda_async::PFRecHitSoAProducerHCAL',
    producers = cms.VPSet(
      cms.PSet(
        params = cms.ESInputTag('', ''),
        src = cms.InputTag('')
      ),
      template = cms.PSetTemplate(
        src = cms.InputTag(''),
        params = cms.ESInputTag('', '')
      )
    ),
    topology = cms.ESInputTag('', ''),
    synchronise = cms.untracked.bool(False),
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
