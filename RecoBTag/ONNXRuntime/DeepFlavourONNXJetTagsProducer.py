import FWCore.ParameterSet.Config as cms

def DeepFlavourONNXJetTagsProducer(**kwargs):
  mod = cms.EDProducer('DeepFlavourONNXJetTagsProducer',
    src = cms.InputTag('pfDeepFlavourTagInfos'),
    input_names = cms.vstring(
      'input_1',
      'input_2',
      'input_3',
      'input_4',
      'input_5'
    ),
    model_path = cms.FileInPath('RecoBTag/Combined/data/DeepFlavourV04_12X_training/DeepJet_Run3_122X.onnx'),
    output_names = cms.vstring('ID_pred/Softmax:0'),
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
