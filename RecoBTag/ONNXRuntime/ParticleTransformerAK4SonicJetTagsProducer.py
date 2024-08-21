import FWCore.ParameterSet.Config as cms

def ParticleTransformerAK4SonicJetTagsProducer(**kwargs):
  mod = cms.EDProducer('ParticleTransformerAK4SonicJetTagsProducer',
    Client = cms.PSet(
      mode = cms.string('PseudoAsync'),
      allowedTries = cms.untracked.uint32(0),
      verbose = cms.untracked.bool(False),
      modelName = cms.required.string,
      modelVersion = cms.string(''),
      modelConfigPath = cms.required.FileInPath,
      preferredServer = cms.untracked.string(''),
      timeout = cms.required.untracked.uint32,
      timeoutUnit = cms.untracked.string('seconds'),
      useSharedMemory = cms.untracked.bool(True),
      compression = cms.untracked.string(''),
      outputs = cms.untracked.vstring()
    ),
    src = cms.InputTag('pfParticleTransformerAK4TagInfos'),
    input_names = cms.vstring(
      'input_1',
      'input_2',
      'input_3',
      'input_4',
      'input_5',
      'input_6'
    ),
    output_names = cms.vstring('softmax'),
    flav_names = cms.vstring(
      'probb',
      'probbb',
      'problepb',
      'probc',
      'probuds',
      'probg'
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
