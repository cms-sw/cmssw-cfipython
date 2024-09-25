import FWCore.ParameterSet.Config as cms

def ECFAdder(*args, **kwargs):
  mod = cms.EDProducer('ECFAdder',
    src = cms.InputTag('no default'),
    Njets = cms.vuint32(
      1,
      2,
      3
    ),
    cuts = cms.vstring(
      '',
      '',
      ''
    ),
    alpha = cms.double(1),
    beta = cms.double(1),
    ecftype = cms.string(''),
    srcWeights = cms.InputTag('puppi'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
